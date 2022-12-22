import React from 'react';
import { List, Datagrid, TextField, FunctionField, Pagination, EditButton} from 'react-admin';
import { SearchInput, TextInput } from 'react-admin';

const PostPagination = props => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} {...props} />;

const postFilters = [
  <TextInput label='resources.operations.fields.name' source="name" alwaysOn />,
];

const OperationsList = (props) => (
  <List {...props} pagination={<PostPagination />} filters={postFilters}  >
    <Datagrid>
      <TextField source='id'  />
      <TextField source='substance.name' label="resources.operations.fields.name"  fullWidth/>
      <FunctionField
        label="resources.operations.fields.user" 
        sortBy="user.surname"
        render={user => `${user.user.name} ${user.user.surname}`}
        fullWidth
      />;
      <TextField source='type.type' sortable={false} label="resources.operations.fields.type"  />
      <TextField source='amount'  />
      <TextField source='date'  />  
      <EditButton/>  
    </Datagrid>
  </List>
);



export default OperationsList;