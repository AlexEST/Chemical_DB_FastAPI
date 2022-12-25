import russianMessages from 'ra-language-russian';

export const messages = {
    ...russianMessages,
    resources: {
        operations: {
            name: 'Операция |||| Операции',
            fields: {
                id: 'Ид.',
                name : 'Название',
                user: 'Имя пользователя',
                type: 'Тип операции',
                amount: 'Количество',
                date: 'Дата',
                createTitle: 'Добавление новой операции',
                columns:'КОЛОНКИ'
            },
        },
        substances: {
            name: 'Вещество |||| Вещества',
            fields: {
                id: 'Ид.',
                name: 'Название',
                element_number: 'Номер элемента',
                cas: 'CAS',
                formula:'Формула',
                units:'Количество',
                type:'Тип вещества',
                createTitle: 'Добавление нового вещества'
            },
        },
        stock: {
            name: 'Склад |||| Склад',
            fields: {
                id: 'Ид.',
                name: 'Название вещества',
                amount: 'Количество',
                units: 'Ед. измерения',
            },
        },
    },
    
};

export default messages;
