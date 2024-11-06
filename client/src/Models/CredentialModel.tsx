export class CredentialModel {
    public password: string;
    last_login!: Date;
    is_superuser!: number;
    public username!: string;
    first_name!: string;
    last_name!: string;
    email: string;
    is_staff!: number;
    is_active!: number;
    date_joined!: Date;
  
    constructor(email: string = "", password: string = "") {
      this.email = email;
      this.password = password;
    }
  }
  