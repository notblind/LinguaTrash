<template>
	<div id="app">
		<div v-if="partner && !addition" class="container">
			<Menu/>
			<router-view/>
		</div>
		<div v-if="!partner && !addition">
			<LogIn/>
		</div>

		<div v-if="addition">
			<Me/>
		</div>
	</div>
</template>

<script>
import Me from '@/views/addition/Me';
import LogIn from '@/views/login/Login';
import Menu from '@/components/Menu';
import RPService from './services/rps';
const rps = new RPService();

export default({
	name: 'mainApp',
	components: {
		Menu,
		LogIn,
		Me
	},
	data() {
		return {
			partner: undefined,
			addition: Boolean
		}
	},
	created() {
		this.addition = false;
		const currentUrl = window.location.pathname;

		if (currentUrl == '/me' || currentUrl == '/me/'){
			this.addition = true;
		} else {
			this.partner = undefined;
			rps.getMe().then((res) => {
				this.partner = res;
			});
		}
	}
});
</script>

<style>
	@import 'styles.scss'
</style>
