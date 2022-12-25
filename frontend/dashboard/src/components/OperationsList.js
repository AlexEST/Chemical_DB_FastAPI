import React from 'react';
import { List, TextField, FunctionField, Pagination, EditButton,  DatagridConfigurable } from 'react-admin';
import { TextInput } from 'react-admin';


const PostPagination = props => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} {...props} />;

const OperationFilters = [
  <TextInput label='resources.operations.fields.name' source="name" alwaysOn />,
];


const OperationsList = (props) => (
  <List {...props} pagination={<PostPagination />} filters={OperationFilters}  >
    <DatagridConfigurable >
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
    </DatagridConfigurable>
  </List>
);



export default OperationsList;