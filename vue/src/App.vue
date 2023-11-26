<template>
	<div id="app">
		<div v-if="!addition" class="container">
			<Menu/>
			<router-view/>
		</div>
	</div>
</template>

<script>
import Menu from '@/components/Menu';
import RPService from './services/rps';
const rps = new RPService();

export default({
	name: 'mainApp',
	components: {
		Menu,
	},
	created() {
		const currentUrl = window.location.pathname;
	}
});
</script>

<style>
	@import 'styles.scss'
</style>
