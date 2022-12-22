import polyglotI18nProvider from 'ra-i18n-polyglot';
import englishMessages from './i18n/en';

//const translations = { en, et, ru };

const messages = {
    ru: () => import('./i18n/ru').then(messages => messages.default),
    en: () => import('./i18n/en').then(messages => messages.default),
    et: () => import('./i18n/est').then(messages => messages.default),
};

const i18nProvider = polyglotI18nProvider(
    locale => {
        if (locale === 'ru') {
            return messages[locale]();
        }
        if (locale === 'et') {
            return messages[locale]();
        }
        // Always fallback on english
        return englishMessages;
    },
    'en',
    
    [
        { locale: 'en', name: 'English' },
        { locale: 'et', name: 'Eesti' },
        { locale: 'ru', name: 'Русский' },
    ],
    { allowMissing: true }
);

export default i18nProvider;