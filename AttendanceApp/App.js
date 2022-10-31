import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { useEffect, useRef, useState } from 'react';
import { Camera } from 'expo-camera';
import { shareAsync } from 'expo-sharing';
import * as MediaLibrary from 'expo-media-library';

export default function App() {

	let cameraRef = useRef();
	// setting the camera and media access permissions 
	const [hasCameraPermission, setHasCameraPermission] = useState();
	const [hasMediaPermission, setHasMediaPermission] = useState();

	useEffect(() => {
		(async() => {
			const CameraPermission = await Camera.requestCameraPermissionsAsync();
			const MediaLibraryPermission = await MediaLibrary.requestPermissionsAsync();
			setHasCameraPermission(CameraPermission.status === "granted");
			setHasMediaLibraryPermission(mediaLibraryPermission.status === "granted");
		})();
	}, []);

	return (
		<View style={styles.container}>
			<Text>Open up App.js to start working on your app!</Text>
			<StatusBar style="auto" />
		</View>
	);
}

// text to display when camera permission not given 
if(hasCameraPermission === undefined)
{
	return <Text>Requesting permissions... </Text>
}
else if(!hasCameraPermission)
{
	return <Text>Permission for Camera not granted</Text>
}

const styles = StyleSheet.create({
	container: {
		flex: 1,
		backgroundColor: '#fff',
		alignItems: 'center',
		justifyContent: 'center',
	},
});
