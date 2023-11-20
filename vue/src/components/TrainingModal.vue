<template>
	<div>
		<div class="back-modal"></div>
		<div class="mat-modal">
			<div class="modal-title" style="flex-wrap: wrap; position: relative;">
				{{vocabulary.name}}: Тренировка
				<span style="width: 100%; font-size: 14px; position: absolute; top: 40px;">{{vocabulary.words.length}} из 400 слов</span>
			</div>
			<div class="modal-form" style="margin-top: 20px;">

				<div class="training">
					<div class="check-training" v-on:click="modes.first=!modes.first">
						<div class="checkBox" v-bind:class="{'checkBox-none': !modes.first}"><font-awesome-icon icon="check" /></div>
						<div>Карточки со словами</div>
					</div>
					<div class="check-training" v-on:click="modes.second=!modes.second">
						<div class="checkBox" v-bind:class="{'checkBox-none': !modes.second}"><font-awesome-icon icon="check" /></div>
						<div>Перевод слов</div>
					</div>
					<div class="check-training" v-on:click="modes.third=!modes.third">
						<div class="checkBox" v-bind:class="{'checkBox-none': !modes.third}"><font-awesome-icon icon="check" /></div>
						<div>Обратный перевод слов</div>
					</div>
				</div>
				<div class="modal-form-btns">
					<button class="btn-cancel" v-on:click="close()">Назад</button>
					<router-link tag="button" class="btn-submit" style="margin-left: 10px;"
						:to="{ name: 'Training', params: {idVocabulary: vocabulary.id, modes: modes}}">Начать</router-link>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Vue from 'vue';
import RPService from '../services/rps';

import { library } from '@fortawesome/fontawesome-svg-core'
import { faCheck } from '@fortawesome/free-solid-svg-icons'
library.add(faCheck)
const rps = new RPService();

export default Vue.extend({
	name: 'TrainingModal',
	props: ['vocabulary'],
	data() {
		return {
			modes: {
				first: true,
				second: true,
				third: true
			},
		};
	},
	computed: {
    idVocabulary() {
      return this.$route.params.idVocabulary;
    },
  },
	methods: {
		close(){
			this.$emit('close');
		}
	}
});
</script>
