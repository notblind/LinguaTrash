<template>
	<div class="login-align">
		<div class="login-center">
			<div class="modal-form" v-if="visLogin">
				<div class="login-logo">
					<span class="logo-1">Lingua</span><span class="logo-2">Trash</span>
				</div>
				<div class="login-text-css">Комфортное обучение</div>
				<input type="text" v-model="user.username" placeholder="Почта">
				<input type="text" v-model="user.password" placeholder="Пароль">
				<div>
				</div>
				<div class="modal-form-btns" style="margin-top: 20px;">
					<button class="button-add" v-on:click="login()">Войти</button>
					<button class="button-add" v-on:click="visLogin=!visLogin">Создать аккаунт</button>
				</div>
			</div>

			<form @submit.prevent="signup" class="modal-form" v-if="!visLogin">
				<input type="text" v-model="user.username" placeholder="Почта">
				<input type="text" v-model="user.password" placeholder="Пароль">
				<div class="modal-form-btns">
					<button class="btn-submit" style="margin-left: 10px;" type="submit">Регистрация</button>
				</div>
			</form>

			<div class="login-text">
				<div class="login-text-style">
					<span>Добрый вечер!</span> <br>
					Вы случайно наткнулись на платформу для запоминания иностранных слов. <br><br>
					Для доступа к платформе нужно всего лишь "Войти"
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Vue from 'vue';
import RPService from '../../services/rps';
import router from  '../../router/index.ts'
const rps = new RPService();

export default Vue.extend({
	name: 'LogIn',
	components: {
	},
	data() {
		return {
			visLogin: Boolean,
			user: {
				'username': null,
				'password': null
			}
		};
	},
	methods: {
		login(){
			rps.logIn(this.user.username, this.user.password).then(res => {
				window.location.replace("http://localhost:8080/");
			});
		},
		signup(){
			rps.signUp(this.user.username, this.user.password).then(res => {
				return;
			});
		}
	}
});
</script>