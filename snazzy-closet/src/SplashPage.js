import React from 'react';
import { Container, Typography, Button, TextField, Box } from '@mui/material';
import { styled } from '@mui/system';

const BackgroundBox = styled(Box)({
  height: '100vh',
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  backgroundImage: 'linear-gradient(120deg, #1D4E89 0%, #87CEEB 100%)', // Metallic Blue to Soft Sky Blue
  textAlign: 'center',
});

const CustomButton = styled(Button)({
  backgroundColor: '#008080', // Bright Teal
  color: '#FFFFFF', // White
  '&:hover': {
    backgroundColor: '#1D4E89', // Metallic Blue
  },
});

const textStyles = {
  color: '#FFFFFF', // White for high contrast
  textShadow: '1px 1px 3px rgba(0, 0, 0, 0.5)', // Subtle shadow for better readability
};

function LaunchSplashPage() {
  return (
    <BackgroundBox>
      <Container maxWidth="sm">
        <Typography variant="h2" component="h1" gutterBottom style={{ ...textStyles, fontWeight: 'bold' }}>
          Snazzy Closet
        </Typography>
        <Typography variant="h5" component="p" gutterBottom style={textStyles}>
          Your Personalized Fashion Recommender
        </Typography>
        <Typography variant="body1" component="p" gutterBottom style={textStyles}>
          Get ready for a stylish experience tailored just for you. Sign up to be the first to know when we launch!
        </Typography>
        <TextField
          variant="outlined"
          placeholder="Enter your email"
          fullWidth
          margin="normal"
          InputProps={{ style: { backgroundColor: '#FFFFFF', borderRadius: '4px' } }}
        />
        <CustomButton
          variant="contained"
          size="large"
          fullWidth
          style={{ marginTop: '20px', padding: '10px' }}
        >
          Join the Waitlist
        </CustomButton>
      </Container>
    </BackgroundBox>
  );
}

export default LaunchSplashPage;
