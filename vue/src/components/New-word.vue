<template>
	<div>
		<div class="back-modal"></div>
		<div class="mat-modal big-modal">
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
					<button class="btn-cancel" v-on:click="close()">Назад</button>
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
const rps = new RPService();

export default Vue.extend({
	name: 'NewWord',
	props: ['idVocabulary'],
	data() {
		return {
			newWord: {
				vocabulary: this.idVocabulary,
				word: null,
				translations: ['', '', '', '', '']
			}
		};
	},
	methods: {
		addPhrase(cancel) {
			console.info(this.idVocabulary);
			if (this.newWord.word.trim()){
				rps.createWord(this.newWord).then(() => {
					this.$emit('getData');
					this.newWord.word = '';
					this.newWord.translations = ['', '', '', '', ''];
					if (cancel){
						this.close();
					}
				});
			}
		},
		close(){
			this.$emit('close');
		}
	}
});
</script>
