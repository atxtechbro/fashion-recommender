import React from 'react';
import { Container, Typography, Button, TextField, Box } from '@mui/material';
import { styled } from '@mui/system';

const BackgroundBox = styled(Box)({
  height: '100vh',
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  backgroundImage: 'linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%)',
  textAlign: 'center',
});

function LaunchSplashPage() {
  return (
    <BackgroundBox>
      <Container maxWidth="sm">
        <Typography variant="h2" component="h1" gutterBottom>
          Snazzy Closet
        </Typography>
        <Typography variant="h5" component="p" gutterBottom>
          Your Personalized Fashion Recommender
        </Typography>
        <Typography variant="body1" component="p" gutterBottom>
          Get ready for a stylish experience tailored just for you. Sign up to be the first to know when we launch!
        </Typography>
        <TextField
          variant="outlined"
          placeholder="Enter your email"
          fullWidth
          margin="normal"
          InputProps={{ style: { backgroundColor: 'white', borderRadius: '4px' } }}
        />
        <Button
          variant="contained"
          color="primary"
          size="large"
          fullWidth
          style={{ marginTop: '20px', padding: '10px' }}
        >
          Join the Waitlist
        </Button>
      </Container>
    </BackgroundBox>
  );
}

export default LaunchSplashPage;
