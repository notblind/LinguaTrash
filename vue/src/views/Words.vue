<template>
	<div class="home" v-if="vocabulary && words">
		<div class="mat-div">
			<div class="mat-title">
				<div class="mat-name">{{vocabulary.name}}</div>
				<div style="display: flex;">
<!-- 					<div class="button-add" v-on:click="visAddWord = false" style="margin-right: 10px;">Добавить слова</div> -->
					<div class="button-add" v-on:click="visAddPhrase = false">Добавить cлово или словосочетание</div>
				</div>
			</div>
			<ul class="list-ul">
				<li v-for="item in words" :key="item.id" class="list-item">
					<div>
						<div class="list-ul-name">{{item.word}}</div>
					</div>
					<div class="rightpart-list">
						<span v-for="trans in item.translations" :key="trans.id">
							{{trans.translate}}
						</span>
					</div>
				</li>
			</ul>
		</div>

		<NewWord v-bind:idVocabulary="idVocabulary" v-if="!visAddPhrase" @close="visAddPhrase = true" @getData="getData()" />

	</div>
</template>

<script>
import Vue from 'vue';
import RPService from '../services/rps';
import NewWord from '@/components/New-word';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faPlus } from '@fortawesome/free-solid-svg-icons'
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
		}
	}
});
</script>
