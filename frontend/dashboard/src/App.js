import * as React from "react";
import { Admin, Resource, } from 'react-admin';
import simpleRestProvider from 'ra-data-simple-rest';
import OperationsList from "./components/OperationsList";
import OperationCreate from "./components/OperationCreate";
import { fetchUtils } from 'ra-core';
import SubstancesList from "./components/SubstancesList";
import SubstanceCreate from "./components/SubstanceCreate";
import OperationEdit from "./components/OperationEdit";
import SubstanceEdit from "./components/SubstanceEdit";
import authProvider from './components/authProvider';
import StockList from "./components/StockList";
import { Login } from 'react-admin';
import  i18nProvider  from './components/i18nProvider';
import UsersList from "./components/UsersList";
import GroupOutlinedIcon from '@mui/icons-material/GroupOutlined';
import ScienceOutlinedIcon from '@mui/icons-material/ScienceOutlined';
import WarehouseOutlinedIcon from '@mui/icons-material/WarehouseOutlined';
import FormatListBulletedOutlinedIcon from '@mui/icons-material/FormatListBulletedOutlined';

const dataProvider = simpleRestProvider('http://localhost:8000', fetchUtils.fetchJson, 'X-Total-Count');
//



const MyLoginPage = () => <Login backgroundImage="https://haldus.taltech.ee/sites/default/files/styles/manual_crop/public/news-image/TalTech_Zoom_taust_1920x1080px-05_0.jpg?itok=eX-ClB7d" />;

const App = () => (
    <Admin disableTelemetry dataProvider={dataProvider} i18nProvider={i18nProvider}  authProvider={authProvider} loginPage={MyLoginPage} requireAuth >
       <Resource name='operations'  list={OperationsList} create={OperationCreate} edit={OperationEdit} icon={FormatListBulletedOutlinedIcon} />
       <Resource name='substances'  list={SubstancesList} create={SubstanceCreate} edit={SubstanceEdit} icon={ScienceOutlinedIcon} />
       <Resource name='stock'  list={StockList} icon={WarehouseOutlinedIcon}  />
       <Resource name='users'  list={UsersList} icon={GroupOutlinedIcon} />
    </Admin>
);



export default App;

