import axios, {Method} from "axios";
import _ from "lodash";

export default class RPService {

	public _data: any;
	public res: any;
	private _jwtToken: any;
	private mainUrl: string;

	toSnakeCase(obj: any) {
		return _.mapKeys(obj, function (value: any, key: any){
			return _.snakeCase(key);
		})
	}

	constructor() {
		this.mainUrl = "http://localhost:8000/"
		if ("127.0.0.1:8080".includes(window.location.host) || "localhost:8080".includes(window.location.host)){
			this.mainUrl = "http://localhost:8000/";
		} else {
			this.mainUrl = "";
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

	async sendRequest(url: string, method: Method, data?: any, snakeCase?: boolean) {
		if (snakeCase) {
			data = this.toSnakeCase(data)
		}
		const config = {
			method: method,
			url: this.mainUrl + url,
			data: data,
			headers: this._getJWTToken() ? {
				'Authorization': 'Bearer ' + this._getJWTToken(),
			} : {},
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
		bodyFormData.append("username", username);
		bodyFormData.append("password", password);
		bodyFormData.append("email", username);
		return axios.post(this.mainUrl + "auth/users/", bodyFormData)
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

	async getMe() {
		return await this.sendRequest("account/api/v1/user", "GET");
	}

	async getListVocabulary() {
		return await this.sendRequest("vocabulary/api/v1/vocabulary", "GET");
	}

	async createVocabulary(vocabulary: any): Promise<any>{
		this._data = this.sendRequest("vocabulary/api/v1/vocabulary", "POST", vocabulary);
		return this._data
	}

	async getVocabulary(idVocabulary: number) {
		return await this.sendRequest(`vocabulary/api/v1/vocabulary/${idVocabulary}`, "GET");
	}

	async deleteVocabulary(idVocabulary: number) {
		return await this.sendRequest(`vocabulary/api/v1/vocabulary/${idVocabulary}`, "DELETE");
	}

	async editVocabulary(idVocabulary: number, vocabulary: any) {
		return await this.sendRequest(`vocabulary/api/v1/vocabulary/${idVocabulary}`, "PATCH", vocabulary);
	}

	async getWords(idVocabulary: number, vocabulary: any) {
		return await this.sendRequest(
			"vocabulary/api/v1/word", "GET", {vocabularyId: idVocabulary}, true
		);
	}

	async createWord(word: any) {
		return await this.sendRequest("vocabulary/api/v1/word", "POST", word, true);
	}

	async getTraining(idVocabulary: number, mode: string) {
		const data = {
			vocabularyId: idVocabulary,
			mode: mode,
		}
		return await this.sendRequest("vocabulary/api/v1/training", "GET", data, true);
	}

	async createFeedback(text: any) {
		return await this.sendRequest("additional/api/v1/feedback", "POST", {text: text});
	}

	async getHolidays() {
		return await this.sendRequest("additional/api/v1/holiday", "GET");
	}

}
