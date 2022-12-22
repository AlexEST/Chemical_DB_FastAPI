import React, { useState, useEffect } from 'react';
import {
  Form,
  DateInput,
  SelectInput,
  TextInput,
  useGetList,
  AutocompleteInput,
  SaveButton,
  Edit,
  required
} from 'react-admin';


import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import ValidateOperationEdit from './OperationEditValidation';


const OperationEdit = (props) => {
 
  const [substances, setSubstances] = useState([]);
  const { data: substance } = useGetList(
    'substancesNames',
    {
      pagination: { page: 1, perPage: 600 },
      sort: { field: 'name', order: 'ASC' }
    }
  );

  const {id, fullName, avatar } = JSON.parse(localStorage.getItem('auth'));
  const name = String(fullName).replace("[", "").replace("]", "")
  

  useEffect(() => { 
    if (substance)
      setSubstances(substance.map((d) => ({ id: d.name, name: d.name })));
  }, [substance]);


  return (
    <Edit {...props} title='Edit Operation' redirect='/operations' >
      <Form validate={ValidateOperationEdit}>
        <Box margin={5} maxWidth={400}>
        <Grid container direction='column' spacing={2}  justifyContent="center">
          <Grid>
            <AutocompleteInput  source="substance.name" label='resources.operations.fields.name'  variant='outlined' fullWidth choices={substances} validate={required}/>  
          </Grid>
          <Grid >
            <TextInput source="" label='resources.operations.fields.user' variant='outlined' disabled fullWidth defaultValue={name} validate={required}/>
          </Grid>
          <Grid >
            <SelectInput
              source='type.type'
              variant='outlined'
              label = 'resources.operations.fields.type'
              fullWidth
              validate={required}
              defaultValue=''
              choices={[
                { id: 'Add', name: 'Add' },
                { id: 'Remove', name: 'Remove' },
              ]}
            />
          </Grid>
          <Grid>
            <TextInput source='amount' variant='outlined' type='number' fullWidth validate={required} />
          </Grid>
          <Grid>
              <DateInput source='date' fullWidth variant='outlined' validate={required} />
          </Grid>

          <Grid>
            <SaveButton />
          </Grid>

        </Grid>
        </Box>
      </Form>
    </Edit>
  );
};

export default OperationEdit;