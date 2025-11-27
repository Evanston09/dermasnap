import { Colors } from '@/constants/Colors';
import { Drawer } from 'expo-router/drawer';
import { useSession } from '@/contexts/AuthContext';
import { TouchableOpacity, Alert } from 'react-native';
import { ThemedText } from '@/components/ThemedText';
import { LogOut } from 'lucide-react-native';


export default function DrawerLayout() {
    const { signOut } = useSession();

    const handleSignOut = async () => {
        Alert.alert(
            'Sign Out',
            'Are you sure you want to sign out?',
            [
                {
                    text: 'Cancel',
                    style: 'cancel',
                },
                {
                    text: 'Sign Out',
                    style: 'destructive',
                    onPress: async () => {
                        try {
                            await signOut();
                        } catch (error) {
                            Alert.alert('Error', 'Failed to sign out. Please try again.');
                        }
                    },
                },
            ]
        );
    };

    return (
        <Drawer
            screenOptions={{
                drawerActiveTintColor: Colors.primary_700,
                drawerInactiveTintColor: Colors.primary_600,
                drawerType: "slide",
                headerRight: () => (
                    <TouchableOpacity
                        onPress={handleSignOut}
                        style={{ marginRight: 16, flexDirection: 'row', alignItems: 'center', gap: 8 }}
                    >
                        <ThemedText type="defaultSemiBold" style={{ color: Colors.primary_700 }}>
                            Sign Out
                        </ThemedText>
                        <LogOut size={20} color={Colors.primary_700} />
                    </TouchableOpacity>
                ),
            }}
        >
            <Drawer.Screen
                name="index"
                options={{
                    drawerLabel: 'Overview',
                    title: 'Overview',
                }}
            />
            <Drawer.Screen
                name="acneType"
                options={{
                    drawerLabel: 'Analyze Acne Type',
                    title: 'Analyze Acne Type',
                }}
            />
            <Drawer.Screen
                name="findProducts"
                options={{
                    drawerLabel: 'AI-Recommended Products',
                    title: 'AI-Recommended Products',
                }}
            />
        </Drawer>
    );
}
