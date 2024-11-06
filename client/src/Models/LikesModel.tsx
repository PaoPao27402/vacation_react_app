export class LikesModel {
    public user: number;
    public vacation: number;

    constructor(user: number = 0, vacation: number = 0) {
        this.user = user;
        this.vacation = vacation;
    }
}