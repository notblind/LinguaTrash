<template>
	<div class="home" v-if="vocabulary && words" style="margin-bottom:40px; margin-top: 10px;">
		<div class="mat-div">
			<div class="mat-title">
				<div class="mat-name">{{vocabulary.name}}</div>
				<div style="display: flex;">
					<div class="button-add" v-on:click="visDeleteVocab = false" style="margin-right: 10px;">Удалить словарь</div>
					<div class="button-add" v-on:click="visAddPhrase = false">Добавить cлово или словосочетание</div>
				</div>
			</div>
			<ul class="list-ul">
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
import router from  '../router/index.ts'
const rps = new RPService();
library.add(faPlus)

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
			visAddWord: Boolean,
			visAddPhrase: Boolean,
			visDeleteVocab: Boolean,
			vocabulary: null,
			words: null,
			newWords: []
		};
	},
	created() {
		rps.getOneVocabulary(this.idVocabulary).then(res => {
			this.vocabulary = res.data.vocabulary;
		});
		rps.getWords(this.idVocabulary).then(res => {
			this.words = res.data.words;
		});
	},
	methods: {
		getData(){
			rps.getWords(this.idVocabulary).then(res => {
				this.words = res.data.words;
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
