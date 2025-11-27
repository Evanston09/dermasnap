import { SplashScreen } from 'expo-router';
import { useSession } from '@/contexts/AuthContext';

SplashScreen.preventAutoHideAsync();

export default function SplashScreenController() {
  const { isLoading } = useSession();

  if (!isLoading) {
    SplashScreen.hide();
  }

  return null;
}

