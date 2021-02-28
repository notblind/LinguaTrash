import axios from 'axios';

export default class RPService {

	public _data: any;
	public res: any;
	private _jwtToken: any;
	private mainUrl: string;

	constructor() {
		if ('127.0.0.1:8080'.includes(window.location.host)){
			this.mainUrl = 'http://localhost:8000/';
		} else {
			this.mainUrl = 'https://linguatrash.fun/'
		}
	}


	_getJWTToken(){
		if (!this._jwtToken){
			const results = document.cookie.match ( '(^|;) ?' + 'jwt' + '=([^;]*)(;|$)' );
			return results ? results[2] : '';
		} else return this._jwtToken;
	}

	_delJWTToken(){
		const cookieDate = new Date ();
		cookieDate.setTime(cookieDate.getTime() - 1);
		document.cookie = "jwt=; expires=" + cookieDate.toUTCString();
	}

	sendRequest(url: string, method: string, data: any): Promise<any>{
		const config = {
			headers: {
				'Authorization': 'Bearer ' + this._getJWTToken(),
			}
		}
		return axios.post(this.mainUrl + url, {method: method, data: data}, config).catch(function (error) {
		if (error.response) {
			// Request made and server responded
			// console.log(error.response.data);
			// console.log(error.response.status);
			// console.log(error.response.headers);
			if (error.response.status == '401'){
				// TODO: сделать проверку на url  и только тогда редиректить
				window.location.reload(true);
			}
		} else if (error.request) {
			// The request was made but no response was received
			console.log(error.request);
		} else {
			// Something happened in setting up the request that triggered an Error
			console.log('Error', error.message);
		}

	});
	}

	_login(username: any, password: any): Promise<any>{
		const bodyFormData = new FormData();
		bodyFormData.append('username', username);
		bodyFormData.append('password', password);
		return axios.post(this.mainUrl + 'auth/jwt/create', bodyFormData)
	}

	logIn(username: any, password: any){
		this._data = this._login(username, password).then(res =>{
			this._jwtToken = res.data.access;
			if ('127.0.0.1:8080'.includes(window.location.host)){
				document.cookie = "jwt="+ this._jwtToken +"; max-age=604800; samesite=lax; path=/;";
			} else{
				document.cookie = "jwt="+ this._jwtToken +"; max-age=604800; samesite=lax; path=/; secure";
			}
		});
		return this._data
	}

	_sigup(username: any, password: any): Promise<any>{
		const bodyFormData = new FormData();
		bodyFormData.append('username', username);
		bodyFormData.append('password', password);
		bodyFormData.append('email', username);
		return axios.post(this.mainUrl + 'auth/users/', bodyFormData)
	}

	signUp(username: any, password: any){
		this._data = this._sigup(username, password);
		return this._data
	}

	async logOut(): Promise<any>{
		this._jwtToken = undefined;
		await this._delJWTToken();
		return this._data
	}

	getMeOnly(): Promise<any>{
		const config = {
			headers: {
				'Authorization': 'Bearer ' + this._getJWTToken(),
			}
		}
		return axios.post(this.mainUrl + 'api/vocabulary/partner', {method: 'get_me', data: {}}, config)
	}

	getMe(): Promise<any>{
		this._data = this.sendRequest('api/vocabulary/partner', 'get_me', {});
		return this._data
	}

	getVocabulary(isFull?: boolean): Promise<any>{
		this._data = this.sendRequest('api/vocabulary', 'get_vocabulary', {isFull: isFull});
		return this._data
	}

	deleteVocabulary(idVocabulary: number): Promise<any>{
		this._data = this.sendRequest('api/vocabulary', 'delete_vocabulary', {idVocabulary: idVocabulary});
		return this._data
	}

	getOneVocabulary(idVocabulary: number): Promise<any>{
		this._data = this.sendRequest('api/vocabulary', 'get_one_vocabulary', {idVocabulary: idVocabulary});
		return this._data
	}

	getWords(idVocabulary: number): Promise<any>{
		this._data = this.sendRequest('api/vocabulary', 'get_words', {idVocabulary: idVocabulary});
		return this._data
	}

	createVocabulary(vocabulary: any): Promise<any>{
		this._data = this.sendRequest('api/vocabulary', 'create_vocabulary', {vocabulary: vocabulary});
		return this._data
	}

	editVocabulary(vocabulary: any): Promise<any>{
		this._data = this.sendRequest('api/vocabulary', 'edit_vocabulary', {vocabulary: vocabulary});
		return this._data
	}

	createWord(word: any): Promise<any>{
		this._data = this.sendRequest('api/vocabulary', 'create_word', {word: word});
		return this._data
	}

	modeFirst(idVocabulary: number): Promise<any>{
		this._data = this.sendRequest('api/vocabulary/training', 'mode_first', {idVocabulary: idVocabulary});
		return this._data
	}

	modeSecond(idVocabulary: number): Promise<any>{
		this._data = this.sendRequest('api/vocabulary/training', 'mode_second', {idVocabulary: idVocabulary});
		return this._data
	}

	modeTrird(idVocabulary: number): Promise<any>{
		this._data = this.sendRequest('api/vocabulary/training', 'mode_third', {idVocabulary: idVocabulary});
		return this._data
	}

	createFeedback(text: any): Promise<any>{
		this._data = this.sendRequest('api/vocabulary/extra', 'create_feedback', {text: text});
		return this._data
	}

}
