import React from 'react';
import {
  Create,
  Form,
  NumberInput,
  useNotify,
  useRefresh,
  useRedirect,
  TextInput,
  SaveButton
} from 'react-admin';


import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';



const SubstanceCreate = (props) => {
  const notify = useNotify();
  const refresh = useRefresh();
  const redirect = useRedirect();

  const onSuccess = ({ data }) => {
    //Create('add/operations', { data });
    notify(`New substance added!`);
    redirect('/substances');
    refresh();
  };


  return (
    <Create {...props} title='resources.substances.fields.createTitle' redirect='/substances' resource='add/substances' onSubmit={onSuccess}>
      <Form>
        <Box margin={5} maxWidth={400}>
        <Grid container direction='column'  spacing={2}  justifyContent="center">
          <Grid >
            <TextInput fullWidth source="name" label='resources.substances.fields.name' variant='outlined' required />  
          </Grid>
          <Grid  >
            <NumberInput fullWidth source="element_number" label='resources.substances.fields.element_number' min='0' variant='outlined' required/>  
          </Grid>
          <Grid >
            <TextInput fullWidth source="cas" label='resources.substances.fields.cas' variant='outlined' required/>
          </Grid>
          <Grid >
            <TextInput fullWidth source="formula" label='resources.substances.fields.formula' variant='outlined' required/>
          </Grid>
          <Grid >
            <TextInput fullWidth source='units' label='resources.substances.fields.units' variant='outlined' required/>
          </Grid>
          <Grid >
              <TextInput fullWidth source='type' label='resources.substances.fields.type' variant='outlined' required/>
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

export default SubstanceCreate;