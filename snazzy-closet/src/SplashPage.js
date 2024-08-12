import React from 'react';
import { Container, Typography, Button, Box, TextField } from '@mui/material';
import { styled } from '@mui/system';

const HeroBox = styled(Box)({
  height: '100vh',
  display: 'flex',
  flexDirection: 'column',
  justifyContent: 'center',
  alignItems: 'center',
  backgroundImage: 'linear-gradient(120deg, #1D4E89 0%, #87CEEB 100%)', // Brand colors
  textAlign: 'center',
  color: '#FFFFFF',
  padding: '0 20px',
});

const HeroButton = styled(Button)({
  backgroundColor: '#008080', // Bright Teal
  color: '#FFFFFF',
  '&:hover': {
    backgroundColor: '#1D4E89', // Metallic Blue
  },
  marginTop: '20px',
  padding: '10px 20px',
});

const HeroImage = styled(Box)({
  marginTop: '40px',
  width: '100%',
  maxWidth: '600px',
  height: 'auto',
  backgroundSize: 'cover',
  backgroundPosition: 'center',
});

const EmailTextField = styled(TextField)({
  marginTop: '20px',
  backgroundColor: '#FFFFFF',
  borderRadius: '4px',
  width: '100%',
  maxWidth: '400px',
});

function HeroSection() {
  return (
    <HeroBox>
      <Typography variant="h3" component="h1" gutterBottom>
        Own the Room.
      </Typography>
      <Typography variant="h5" component="p" gutterBottom>
        AI-Driven Style, Unstoppable Confidence.
      </Typography>
      <Typography variant="body1" component="p" gutterBottom>
        Elevate your look. Conquer your day. Snazzy Closet's got you covered.
      </Typography>

      {/* Email capture input */}
      <EmailTextField
        variant="outlined"
        placeholder="Enter your email"
        fullWidth
        margin="normal"
        InputProps={{ style: { backgroundColor: '#FFFFFF', borderRadius: '4px' } }}
      />

      {/* Call to action button */}
      <HeroButton variant="contained" size="large">
        Join the Waitlist
      </HeroButton>

      {/* Placeholder for the Hero Image or Visual */}
      <HeroImage
        style={{
          backgroundImage: `url('path_to_your_image_or_graphic')`,
        }}
      />
    </HeroBox>
  );
}

export default HeroSection;
