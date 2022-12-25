import englishMessages from 'ra-language-english';

export const messages = {
    ...englishMessages,
    resources: {
        operations: {
            name: 'Operation |||| Operations',
            fields: {
                id: 'Id',
                name : 'Substance',
                user: 'User',
                type: 'Operation type',
                amount: 'Amount',
                date: 'Date',
                createTitle: 'Creation of a new operation',
            },
        },
        substances: {
            name: 'Substance |||| Substances',
            fields: {
                id: 'Id',
                name: 'Substance',
                element_number: 'Element number',
                cas: 'CAS',
                formula:'Formula',
                units:'Amount',
                type:'Type',
                createTitle: 'Adding new substance'
            },
        },
        stock: {
            name: 'Stock |||| Stock',
            fields: {
                id: 'Id',
                name: 'Substance',
                amount: 'Amount',
                units: 'Units',
            },
        },
    },
    

};

export default messages;