import React from 'react';
import { List, Datagrid, TextField, Pagination, TextInput} from 'react-admin';


const PostPagination = props => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} {...props} />;

const StockFilters = [
  <TextInput label='resources.stock.fields.name' source="name" alwaysOn />,
];

const StockList = (props) => (
  <List {...props} pagination={<PostPagination />} filters={StockFilters} >
    <Datagrid bulkActionButtons = {false}>
      <TextField source='id'  />
      <TextField source='name' />
      <TextField source='amount'  />
      <TextField source='units'  />  
    </Datagrid>
  </List>
);

export default StockList;