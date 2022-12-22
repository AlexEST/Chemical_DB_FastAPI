import i18nProvider from "./i18nProvider";
import { fetchUtils } from 'ra-core';
import simpleRestProvider from 'ra-data-simple-rest';


const dataProvider = simpleRestProvider('http://localhost:8000', fetchUtils.fetchJson, 'X-Total-Count');


const ValidateOperationEdit = async (values) => {

    const errors = {};

    if (!values.substance) {
        const locale = String(i18nProvider.getLocale())
        if (locale === 'en') {
            errors.substance.name = 'The substance is required';
        } else if (locale === 'ru') {
            errors.substance.name = 'Выберите название вещества';
        } else {
            errors.substance.name = 'Valige aine nimi';
        }

    }
    if (!values.type) {
        const locale = String(i18nProvider.getLocale())
        if (locale === 'en') {
            errors.type.type = 'Type operation is required';
        } else if (locale === 'ru') {
            errors.type.type = 'Выберите тип операции';
        } else {
            errors.type.type = 'Valige operatsiooni tüüp';
        }
    }
    if (!values.amount) {
        const locale = String(i18nProvider.getLocale())
        if (locale === 'en') {
            errors.amount = 'Amount is required';
        } else if (locale === 'ru') {
            errors.amount = 'Введите количество';
        } else {
            errors.amount = 'Nõutav kogus.';
        }
    }



    if (!values.date) {
        const locale = String(i18nProvider.getLocale())
        if (locale === 'en') {
            errors.date = 'Date is required';
        } else if (locale === 'ru') {
            errors.date = 'Введите дату';
        } else {
            errors.date = 'Sisestage kuupäev';
        }
    }


    if (values.amount && values.substance.name && values.type.type === 'Remove') {
        const { data: db } = await dataProvider.getList('stock/substance', {
            pagination: { page: 1, perPage: 1 },
            sort: { field: 'id', order: 'ASC' },
            filter: { name: values.substance.name },
        });
        if ((db.amount - Math.abs(values.amount)) < 0) {
            const locale = String(i18nProvider.getLocale())
            if (locale === 'en') {
                errors.amount = 'Not available in this quantity';
            } else if (locale === 'ru') {
                errors.amount = 'Превышение допустимого количествa. Проверьте остаток.';
            } else {
                errors.amount = 'Lubatud koguse ületamine.';
            }

        }

    }

    return errors
};

export default ValidateOperationEdit;