import React from 'react';
import { List, Datagrid, TextField, Pagination, } from 'react-admin';


const PostPagination = props => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} {...props} />;






const UsersList = (props) => (
  <List {...props} pagination={<PostPagination />}  >
    <Datagrid bulkActionButtons = {false}>
      <TextField source='id'  />
      <TextField source='name' />
      <TextField source='surname'  />  
    </Datagrid>
  </List>
  );

export default UsersList;