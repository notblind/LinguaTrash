<template> 
	<div id="app">
		<div v-if="partner" class="container">
			<Menu/>
			<router-view/>
		</div>
		<div v-if="!partner">
			<LogIn/>
		</div>
	</div>
</template>

<script>
import LogIn from '@/views/login/Login';
import Menu from '@/components/Menu';
import RPService from './services/rps';
const rps = new RPService();

export default({
	name: 'mainApp',
	components: {
		Menu,
		LogIn,
	},
	data() {
		return {
			partner: Boolean,
		}
	},
	created() {
		this.partner = undefined;
		rps.getMeOnly().then((res) => {
			console.info(res);
			this.partner = res.data.partner;
		});
	}
});
</script>

<style>
	@import 'styles.scss'
</style>
