<template>
	<div class="home" style="margin-bottom:60px; margin-top: 10px;">
		<div class="mat-div">
			<div class="mat-title">
				<div class="mat-name">Обратная связь</div>
				<div>
				</div>
			</div>
			<div class="feedback">
				<div class="feedback-text">
					Оставьте тут свой отзыв или предложение :)
				</div>
				<form @submit.prevent="addFeedback" class="feedback-form">
					<textarea  cols="6" type="text" v-model="comment" placeholder="Ваш отзыв">
					</textarea>
					<div class="modal-form-btns">
						<button class="button-add" type="submit">Отправить</button>
					</div>
				</form>
			</div>
		</div>

		<div class="back-modal" v-if="!visClose"></div>
		<div class="mat-modal" v-if="!visClose">
			<div class="modal-title">
				Ваш отзыв отправлен
			</div>
			<div class="modal-form">
				<div class="modal-form-btns">
					<button class="btn-submit" v-on:click="visClose=true">Хорошо</button>
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
	name: 'Feedback',
	components: {
	},
	data() {
		return {
			comment: '',
			visClose: Boolean
		};
	},
	methods: {
		addFeedback() {
			if (this.comment.trim()){
				rps.createFeedback(this.comment).then(() => {
					this.visClose = false;
					this.comment = '';
				});
			}
		}
	}
});
</script>
