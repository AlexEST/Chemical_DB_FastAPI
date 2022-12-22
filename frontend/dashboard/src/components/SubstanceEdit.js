import React from 'react';
import {
  Form,
  NumberInput,
  TextInput,
  SaveButton,
  Edit
} from 'react-admin';


import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';



const SubstanceEdit = (props) => {
  
  return (
    <Edit {...props} title='Edit substance' redirect='/substances' >
      <Form>
        <Box margin={5} maxWidth={400}>
        <Grid container direction='column'   spacing={2}  justifyContent="center">
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
    </Edit>
  );
};

export default SubstanceEdit;