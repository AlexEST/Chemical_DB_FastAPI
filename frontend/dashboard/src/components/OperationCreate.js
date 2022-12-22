import React, { useState, useEffect } from 'react';
import {
  Create,
  Form,
  DateInput,
  SelectInput,
  useNotify,
  useRefresh,
  useRedirect,
  TextInput,
  useGetList,
  AutocompleteInput,
  SaveButton,
  required,
} from 'react-admin';

import ValidateOperationCreation from './OperationCreateValidation';

import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';



const OperationCreate = (props) => {
  const notify = useNotify();
  const refresh = useRefresh();
  const redirect = useRedirect();

  const onSuccess = ({ data }) => {
    console.log(data)
    //Create('add/operations', { data });
    notify(`New operation added!`);
    redirect('/#/operations');
    refresh();
  };

  const [substances, setSubstances] = useState([]);
  const { data: substance } = useGetList(
    'substancesNames',
    {
      pagination: { page: 1, perPage: 600 },
      sort: { field: 'name', order: 'ASC' }
    }
  );

  const [users, setUsers] = useState([]);
  const { data: user } = useGetList(
    'users',
    {
      pagination: { page: 1, perPage: 600 },
      sort: { field: 'surname', order: 'ASC' }
    }
  );

  const { id, fullName, avatar } = JSON.parse(localStorage.getItem('auth'));
  const name = String(fullName).replace("[", "").replace("]", "")


  useEffect(() => {
    if (user)
      setUsers(user.map((d) => ({ id: d.surname, name: d.surname })));
    if (substance)
      setSubstances(substance.map((d) => ({ id: d.name, name: d.name })));
  }, [user, substance]);


  return (
    <Create {...props} title='resources.operations.fields.createTitle' redirect='/operations' resource='add/operations' onSubmit={onSuccess}>
      <Form validate={ValidateOperationCreation}>
        <Box margin={5} maxWidth = {400}>
          <Grid container direction='column' spacing={2} justifyContent="center">
            <Grid>
              <AutocompleteInput source="substance" label='resources.operations.fields.name' variant='outlined' fullWidth choices={substances} validate={required} />
            </Grid>
            <Grid >
              <TextInput source="user" label='resources.operations.fields.user' variant='outlined' fullWidth disabled defaultValue={name} />
            </Grid>
            <Grid>
              <SelectInput
                source='type'
                variant='outlined'
                label='resources.operations.fields.type'
                defaultValue=''
                validate={required}
                fullWidth
                choices={[
                  { id: 'Add', name: 'Add' },
                  { id: 'Remove', name: 'Remove' },
                ]}
              />
            </Grid>
            <Grid>
              <TextInput source='amount' label='resources.operations.fields.amount' variant='outlined' type='number' fullWidth validate={required}/>
            </Grid>
            <Grid >
              <DateInput source='date' label='resources.operations.fields.date' variant='outlined' fullWidth validate={required} />
            </Grid>

            <Grid>
              <SaveButton />
            </Grid>

          </Grid>
        </Box>
      </Form>
    </Create>
  );
};

export default OperationCreate;