import estonianMessages from 'ra-language-estonian';

export const messages = {
    ...estonianMessages,
    resources: {
        operations: {
            name: 'Operatsioon |||| Operatsioonid',
            fields: {
                id: 'Id',
                name : 'Aine',
                user: 'Kasutaja',
                type: 'Operatsiooni tüüp',
                amount: 'Kogus',
                date: 'Kuupäev',
                createTitle: 'Uue operatsiooni loomine',
                columns: 'VEERUD'
            },
        },
        substances: {
            name: 'Aine |||| Ained',
            fields: {
                id: 'Id',
                name: 'Aine',
                element_number: 'Elemendi number',
                cas: 'CAS',
                formula:'Valem',
                units:'Kogus',
                type:'Tüüp',
                createTitle: 'Uue elemendi lisamine'
            },
        },
        stock: {
            name: 'Ladu |||| Ladu',
            fields: {
                id: 'Id',
                name: 'Aine',
                amount: 'Kogus',
                units: 'Ühikud',
            },
        },
        users: {
            name: 'Kasutaja |||| Kasutajad',
            fields: {
                id: 'Id',
                name: 'Nimi',
                surname: 'Perekonnanimi',
            },
        },
    },
    
};

export default messages;