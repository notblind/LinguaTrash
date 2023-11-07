<template>
	<div class="home" style="margin-bottom:60px; margin-top: 10px;">

		<div class="loader" v-if="!vocabulary || !words"></div>

		<div class="mat-div" v-if="vocabulary && words">
			<div class="mat-title">
				<div class="mat-name">{{vocabulary.name}}</div>
				<div style="display: flex;">
					<div class="button-add button-add-mobile" v-on:click="visDeleteVocab = false">
						<font-awesome-icon icon="trash" />
					</div>
				</div>
			</div>
			<ul class="list-ul">
				<div class="list-item add-vocab-box"
					v-on:mouseover="hover2=false" style="height: 70px; min-height: 70px;     border-bottom: solid 1px #e6e6e6;"
					v-on:mouseleave="hover2=true" v-on:click="visAddPhrase = false">
					<div  style="background: #e6e6e6; position: absolute; width: 100%; height: 100%; transition: 0.5s"
					v-bind:style="{ opacity: !hover2 ? '0.0' : '0.5'}"></div>

					<font-awesome-icon style="margin-right: 15px;" icon="plus" size="2x"/>

					<div v-if="!words || words.length == 0">Добавить первое cлово или словосочетание</div>
				</div>

				<li v-for="item in words" :key="item.id" class="list-item">
					<div>
						<div class="list-ul-name">{{item.word}}</div>
					</div>
					<div class="rightpart-list">
						<span v-for="trans in item.translations" :key="trans.id" style="margin-left: 20px;">
							{{trans.translate}}
						</span>
					</div>
				</li>
			</ul>
		</div>

		<NewWord v-bind:idVocabulary="idVocabulary" v-if="!visAddPhrase" @close="visAddPhrase = true" @getData="getData()" />

		<div class="back-modal" v-if="!visDeleteVocab"></div>
		<div class="mat-modal" v-if="!visDeleteVocab">
			<div class="modal-title">
				Удалить словарь?
			</div>
			<div class="modal-form">
				<div class="modal-form-btns">
					<button class="btn-cancel" v-on:click="visDeleteVocab = true">Назад</button>
					<button class="btn-submit" v-on:click="deleteVocab()" style="margin-left: 10px;">Удалить</button>
				</div>
			</div>
		</div>

	</div>
</template>

<script>
import Vue from 'vue';
import RPService from '../services/rps';
import NewWord from '@/components/New-word';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faPlus } from '@fortawesome/free-solid-svg-icons'
import { faTrash } from '@fortawesome/free-solid-svg-icons'
import router from  '../router/index.ts'
const rps = new RPService();
library.add(faPlus)
library.add(faTrash)

export default Vue.extend({
	name: 'Home',
	components: {
		NewWord
	},
	computed: {
    idVocabulary() {
      return this.$route.params.idVocabulary;
    },
  },
	data() {
		return {
			hover2: Boolean,
			visAddWord: Boolean,
			visAddPhrase: Boolean,
			visDeleteVocab: Boolean,
			vocabulary: null,
			words: null,
			newWords: []
		};
	},
	created() {
		rps.getVocabulary(this.idVocabulary).then(res => {
			this.vocabulary = res;
		});
		rps.getWords(this.idVocabulary).then(res => {
			this.words = res;
		});
	},
	methods: {
		getData(){
			rps.getWords(this.idVocabulary).then(res => {
				this.words = res;
			});
		},
		deleteVocab(){
			rps.deleteVocabulary(this.idVocabulary).then(res => {
				router.push({ name: 'Home' })
			});
		}
	}
});
</script>
