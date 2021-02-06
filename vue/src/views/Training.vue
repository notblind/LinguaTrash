<template>
	<div class="home" style="margin-bottom:40px; margin-top: 10px;">
		<div class="mat-div">
			<div class="mat-title">
				<div class="mat-name">Тренировка</div>
				<div class="button-add" style="margin-bottom: 10px;">Закончить досрочно
				</div>
			</div>
		</div>

		<div class="training-box" v-if="currentItem">
			<div class="training-box-item" v-on:mouseover="hover2=true" v-on:mouseleave="hover2=false"
				v-on:click="currentIndex!=0 ? prevWord() : ''"
				v-bind:style="{ 'cursor': currentIndex!=0 ?  'pointer' : ''}">
				<div class="training-back button-add" v-if="currentIndex!=0"
					v-bind:class="{ 'button-add-hov': hover2}">Предыдущее слово</div>
				<div class="training-solve">
					{{currentItem.word}}
				</div>
			</div>

			<div class="training-box-item" v-on:mouseover="hover1=true" v-on:mouseleave="hover1=false"
				v-on:click="currentMode=='first' ? nextWord() : ''"
				style="cursor: pointer;">

				<div class="training-next button-add" 
					v-if="currentIndex+1!=training.length && (currentMode=='first' || ch)" v-bind:class="{ 'button-add-hov': hover1}">Следующее слово</div>

				<div class="training-next button-add" 
					v-if="currentIndex+1==training.length && (currentMode=='first' || ch)" v-bind:class="{ 'button-add-hov': hover1}">Дальше</div>
				<div class="training-solve" v-if="currentMode=='first'" style="text-align: center;">
					<div v-for="trans in currentItem.translations" :key="trans.id">
						{{trans.translate}}
					</div>
				</div>
				<div class="training-solve-ch" v-if="currentMode=='second' || currentMode=='third'">
					<div v-for="(item, index) in currentItem.options" :key="item.option"
						v-on:click="!ch ? ch = item : nextWord()"
						v-bind:style="{ 'height': 'calc(100% / ' + String(currentItem.options.length) + ')',
						'background': ch && item.right ? '#98FB98' : ch==item && !item.right ? '#FFA07A' : '',
						'width': ch ? '700px' : ''}">
						{{index+1}}. {{item.option}}
					</div>
				</div>
			</div>
		</div>

		<div class="back-modal" v-if="!visClose"></div>
		<div class="mat-modal" v-if="!visClose">
			<div class="modal-title">
				Тренировка завершена
			</div>
			<div class="modal-form">
				<div class="modal-form-btns">
					<button class="btn-cancel" v-on:click="endTraining()">Завершить</button>
					<button class="btn-submit" v-on:click="init()" style="margin-left: 10px;">Повторить еще раз</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import Vue from 'vue';
import RPService from '../services/rps';
const rps = new RPService();
import router from  '../router/index.ts'

export default Vue.extend({
	name: 'Training',
	components: {
	},
	props: ['modes'],
	computed: {
    idVocabulary() {
      return this.$route.params.idVocabulary;
    },
  },
  data() {
		return {
			visClose: Boolean,
			hover1: Boolean,
			hover2: Boolean,
			currentMode: null,
			currentItem: null,
			ch: null,
			currentIndex: Number,
			training: []
		};
	},
	created() {
		this.hover1 = false;
		this.hover2 = false;
		this.changeMode();
	},
	methods: {
		init(){
			this.visClose = true;
			this.hover1 = false;
			this.hover2 = false;
			this.currentMode = null,
			this.currentItem = null,
			this.ch = null,
			this.currentIndex = undefined,
			this.training = []
			this.changeMode();
		},
		changeMode(){
			this.ch = false;
			if (this.currentMode=='first'){
				if (!this.modes || this.modes.second){
					this.currentMode='second'
				} else if (this.modes.third){
					this.currentMode='third'
				} else {
					this.visClose = false;
				}
			} else if (this.currentMode=='second'){
				if (!this.modes || this.modes.third){
					this.currentMode='third'
				} else {
					this.visClose = false;
				}
			} else if (this.currentMode=='third'){
				this.visClose = false;
			} else {
				if (!this.modes || this.modes.first){
					this.currentMode='first'
				} else 
				if (this.modes.second){
					this.currentMode='second'
				} else if (this.modes.third){
					this.currentMode='third'
				} else {
					this.visClose = false;
				}
			}
			this.startMode();
		},
		startMode(){
			if (this.currentMode=='first'){
				this.modeFirst();
			} else if (this.currentMode=='second'){
				this.modeSecond();
			} else if (this.currentMode=='third'){
				this.modeTrird();
			}
		},
		modeFirst(){
			rps.modeFirst(this.idVocabulary).then(res => {
				this.training = res.data.training;
				if (this.training && this.training.length > 0){
					this.currentItem = this.training[0];
					this.currentIndex = 0;
				}
			});
		},
		modeSecond(){
			rps.modeSecond(this.idVocabulary).then(res => {
				this.training = res.data.training;
				if (this.training && this.training.length > 0){
					this.currentItem = this.training[0];
					this.currentIndex = 0;
				}
			});
		},
		modeTrird(){
			rps.modeTrird(this.idVocabulary).then(res => {
				this.training = res.data.training;
				if (this.training && this.training.length > 0){
					this.currentItem = this.training[0];
					this.currentIndex = 0;
				}
			});
		},
		endTraining(){
			router.push({ name: 'Home' })
		},
		nextWord(){
			this.currentIndex += 1;
			if (this.currentIndex == this.training.length){
				this.changeMode();
			} else {
				this.currentItem = this.training[this.currentIndex];
			}
			this.ch = false;
		},
		prevWord(){
			this.ch = false;
			this.currentIndex -= 1;
			this.currentItem = this.training[this.currentIndex];
		}
	}
});
</script>