import React from 'react';
import { Container, Typography, Button } from '@mui/material';
import { Google as GoogleIcon, Facebook as FacebookIcon } from '@mui/icons-material';

function SplashPage() {
  return (
    <Container maxWidth="md" style={{ textAlign: 'center', marginTop: '10%' }}>
      <Typography variant="h2" component="h1" gutterBottom>
        Snazzy Closet
      </Typography>
      <Typography variant="h5" component="p" gutterBottom>
        Your Personalized Fashion Recommender
      </Typography>
      <Typography variant="body1" component="p" style={{ marginTop: '20px', marginBottom: '40px' }}>
        Get stylish recommendations for your outfits in a snap!
      </Typography>
      <div>
        <Button
          variant="contained"
          color="primary"
          startIcon={<GoogleIcon />}
          style={{ marginRight: '10px' }}
          onClick={() => alert('Google Sign-In')}
        >
          Sign in with Google
        </Button>
        <Button
          variant="contained"
          color="primary"
          startIcon={<FacebookIcon />}
          onClick={() => alert('Facebook Sign-In')}
        >
          Sign in with Facebook
        </Button>
      </div>
    </Container>
  );
}

export default SplashPage;
