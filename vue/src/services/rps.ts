import axios, {Method} from 'axios';

export default class RPService {

	public _data: any;
	public res: any;
	private _jwtToken: any;
	private mainUrl: string;

	constructor() {
		if ('127.0.0.1:8080'.includes(window.location.host) || 'localhost:8080'.includes(window.location.host)){
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

	async sendRequestNew(url: string, method: Method, data?: any) {
		const config = {
			method: method,
			url: this.mainUrl + url,
			data: data,
			headers: {
				'Authorization': 'Bearer ' + this._getJWTToken(),
			},
			params: method === "GET" ? data : {},
		}
		const res = await axios(config)
		return res.data
	}

	_login(username: any, password: any): Promise<any>{
		const bodyFormData = new FormData();
		bodyFormData.append('username', username);
		bodyFormData.append('password', password);
		return axios.post(this.mainUrl + 'auth/jwt/create/', bodyFormData)
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

	async getListVocabulary() {
		return await this.sendRequestNew("vocabulary/api/v1/vocabulary", "GET");
	}

	async createVocabulary(vocabulary: any): Promise<any>{
		this._data = this.sendRequestNew("vocabulary/api/v1/vocabulary", "POST", vocabulary);
		return this._data
	}

	async getVocabulary(idVocabulary: number) {
		return await this.sendRequestNew(`vocabulary/api/v1/vocabulary/${idVocabulary}`, "GET");
	}

	async deleteVocabulary(idVocabulary: number) {
		return await this.sendRequestNew(`vocabulary/api/v1/vocabulary/${idVocabulary}`, "DELETE");
	}

	async editVocabulary(idVocabulary: number, vocabulary: any) {
		return await this.sendRequestNew(`vocabulary/api/v1/vocabulary/${idVocabulary}`, "PATCH", vocabulary);
	}

	async getWords(idVocabulary: number, vocabulary: any) {
		return await this.sendRequestNew('vocabulary/api/v1/word', "GET", {vocabulary: idVocabulary});
	}

	async createWord(word: any) {
		return await this.sendRequestNew('vocabulary/api/v1/word', "POST", word);
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

	getHolidays(): Promise<any>{
		this._data = this.sendRequest('api/vocabulary/extra', 'get_holidays', {});
		return this._data
	}

}
