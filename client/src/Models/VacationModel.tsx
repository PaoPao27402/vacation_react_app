import { CountryModel } from './CountriesModel';

export class VacationModel {
    public vacationId!: number;
    public countryId!: number; 
    public description!: string;
    public startDate!: string;
    public endDate!: string;
    public price!: number;
    public VacationPicture!: string;
    public country!: CountryModel;
}

export function convertDate(dateString: string): Date {
    const [day, month, year] = dateString.split('/').map(Number);
    return new Date(year, month - 1, day);
  }