import React from 'react';
import { List, Datagrid, TextField, Pagination, EditButton, TextInput} from 'react-admin';


const PostPagination = props => <Pagination rowsPerPageOptions={[5, 10, 25, 50]} {...props} />;

const Filters = [
  <TextInput label='resources.substances.fields.name' source="name" alwaysOn />,
];


const SubstancesList = (props) => (
  <List {...props} pagination={<PostPagination />} filters={Filters} >
    <Datagrid>
      <TextField source='id'  />
      <TextField source='name' />
      <TextField source='element_number' />
      <TextField source='cas'  sortable={false} />
      <TextField source='formula'  sortable={false} />
      <TextField source='units'  sortable={false} />
      <TextField source='type'  />
      <EditButton/>     
    </Datagrid>
  </List>
  );

export default SubstancesList;