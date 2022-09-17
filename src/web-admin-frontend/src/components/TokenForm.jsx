import * as React from 'react';
import IconButton from '@mui/material/IconButton';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputLabel from '@mui/material/InputLabel';
import InputAdornment from '@mui/material/InputAdornment';
import FormControl from '@mui/material/FormControl';
import ContentCopyIcon from '@mui/icons-material/ContentCopy';


export default function TokenForm() {

    const [values, setValues] = React.useState({

      });

      const handleChange = (prop) => (event) => {
      };
    
      const handleClickShowPassword = () => {
        setValues({
        });
      };
    
      const handleMouseDownPassword = (event) => {
        event.preventDefault();
      };

    return (
            <FormControl sx={{ m: 1, width: '600px' }} variant="outlined">
                <InputLabel htmlFor="Token">Token</InputLabel>
                <OutlinedInput
                    id="Token"
                    value={values.password}
                    onChange={handleChange()}
                    endAdornment={
                        <InputAdornment position="end">
                            <IconButton
                                aria-label="token"
                                onClick={handleClickShowPassword}
                                onMouseDown={handleMouseDownPassword}
                                edge="end"
                            >
                                <ContentCopyIcon />
                            </IconButton>
                        </InputAdornment>
                    }
                    label="Token"
                />
            </FormControl>
  )
}
