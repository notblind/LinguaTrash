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

		<div class="back-modal" v-if="!visAddPhrase"></div>
		<div class="mat-modal big-modal" v-if="!visAddPhrase">
			<div class="modal-title">
				Добавить cловосочетание
			</div>
			<div class="modal-form">

				<div class="add-words">
					<div class="add-words-translate">
						<input type="text" v-model="newWord.word" placeholder="Словосочетание">
					</div>
					<div class="modal-title">
						Перевод словосочетания
					</div>
					<div class="add-words-translate">
						<input type="text" v-model="newWord.translations[0]" placeholder="Возможный перевод №1">
						<input type="text" v-model="newWord.translations[1]" placeholder="Возможный перевод №2">
						<input type="text" v-model="newWord.translations[2]" placeholder="Возможный перевод №3">
						<input type="text" v-model="newWord.translations[3]" placeholder="Возможный перевод №4">
						<input type="text" v-model="newWord.translations[4]" placeholder="Возможный перевод №5">
					</div>
				</div>
				<div class="modal-form-btns">
					<button class="btn-cancel" v-on:click="visAddPhrase = true">Назад</button>
					<button class="btn-submit" v-on:click="addPhrase(true)" style="margin-left: 10px;">Сохранить</button>
					<button class="btn-submit" v-on:click="addPhrase(false)" style="margin-left: 10px;">Сохранить и добавить ещё</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Vue from 'vue';
import RPService from '../services/rps';
import { library } from '@fortawesome/fontawesome-svg-core'
import { faPlus } from '@fortawesome/free-solid-svg-icons'
const rps = new RPService();
library.add(faPlus)

export default Vue.extend({
	name: 'Home',
	components: {
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
			newWords: [],
			newWord: {
				vocabulary: this.$route.params.idVocabulary,
				word: null,
				translations: ['', '', '', '', '']
			}
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
		addPhrase(cancel) {
			if (this.newWord.word.trim()){
				rps.createWord(this.newWord).then(() => {
					rps.getWords(this.idVocabulary).then(res => {
						this.newWord.word = '';
						this.newWord.translations = ['', '', '', '', ''];
						this.words = res.data.words;
						if (cancel){
							this.visAddPhrase = true;
						}
					});
				});
			}
		}
	}
});
</script>
