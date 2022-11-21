import React, { useState, useEffect, useRef } from 'react';
import { Text, View, StyleSheet, TouchableOpacity, Image } from 'react-native';
import Constants from 'expo-constants';
import { Camera, CameraType } from 'expo-camera';
import * as MediaLibrary from 'expo-media-library';
import { MaterialIcons } from '@expo/vector-icons';
import Button from './src/components/Button';

import { initializeApp } from 'firebase/app';
import { getFirestore, setDoc, doc } from "firebase/firestore";

export default function App() {

	// setting up firebase for the transfer of images 
	const firebaseConfig = {
		apiKey: "AIzaSyC6lEwU-QT4toNNEvWs63jsnKSaIIFuvvo",
		authDomain: "attendancecamera.firebaseapp.com",
		projectId: "attendancecamera",
		storageBucket: "attendancecamera.appspot.com",
		messagingSenderId: "338003251006",
		appId: "1:338003251006:web:ea222a928384aaa255266f",
		measurementId: "G-796BC5GJV1"
	};
	initializeApp(firebaseConfig);

	const firestore = getFirestore();

	// setting up the camera permissions
	const [hasCameraPermission, setHasCameraPermission] = useState(null);
	const [image, setImage] = useState(null);

	// use the back or the front camera 
	const [type, setType] = useState(Camera.Constants.Type.back);

	// use the camera flash 
	const [flash, setFlash] = useState(Camera.Constants.FlashMode.off);

	// a reference of the camera 
	const cameraRef = useRef(null);

	// requesting for the camera permissions, async as we have to wait for permissions
	useEffect(() => {
		(async () => {
			MediaLibrary.requestPermissionsAsync();
			const cameraStatus = await Camera.requestCameraPermissionsAsync();
			setHasCameraPermission(cameraStatus.status === 'granted');
		})();
	}, []);

	// the function to take pictures 
	const takePicture = async () => {
		if (cameraRef) {
			try {
				const data = await cameraRef.current.takePictureAsync();
				console.log(data);
				setImage(data.uri);
			} catch (error) {
				console.log(error);
			}
		}
	};

	// the function to save the picture
	const savePicture = async () => {
		if (image) {
			try {
				const asset = await MediaLibrary.createAssetAsync(image);
				alert("Picture saved successfully 🥳");
				setImage(null);
				console.log('Picture saved successfully');
			} catch (error) {
				console.log(error);
			}
		}
	};

	// checking for the camera permissions 
	if (hasCameraPermission === false) {
		return <Text>No access to camera</Text>;
	}

	return (
		<View style={styles.container}>
			{!image ? (
				<Camera
					style={styles.camera}
					type={type}
					ref={cameraRef}
					flashMode={flash}
				>
					<View
						style={{
							flexDirection: 'row',
							justifyContent: 'space-between',
							paddingHorizontal: 20,
						}}
					>
						<Button
							title=""
							icon="retweet"
							onPress={() => {
								setType(
									type === CameraType.back ? CameraType.front : CameraType.back
								);
							}}
						/>
						<Button
							onPress={() =>
								setFlash(
									flash === Camera.Constants.FlashMode.off
										? Camera.Constants.FlashMode.on
										: Camera.Constants.FlashMode.off
								)
							}
							icon="flash"
							color={flash === Camera.Constants.FlashMode.off ? 'gray' : '#fff'}
						/>
					</View>
				</Camera>
			) : (
				<Image source={{ uri: image }} style={styles.camera} />
			)}

			<View style={styles.controls}>
				{image ? (
					<View
						style={{
							flexDirection: 'row',
							justifyContent: 'space-between',
							paddingHorizontal: 50,
						}}
					>
						<Button
							title="Re-take"
							onPress={() => setImage(null)}
							icon="retweet"
						/>
						<Button title="Save" onPress={savePicture} icon="check" />
					</View>
				) : (
					<Button title="Click" onPress={takePicture} icon="camera" />
				)}
			</View>
		</View>
	);
}

// defining the styles of all the buttons and text 
const styles = StyleSheet.create({
	container: {
		flex: 1,
		justifyContent: 'center',
		paddingTop: Constants.statusBarHeight,
		backgroundColor: '#000',
		padding: 8,
	},

	controls: {
		flex: 0.5,
	},

	button: {
		height: 40,
		borderRadius: 6,
		flexDirection: 'row',
		alignItems: 'center',
		justifyContent: 'center',
	},

	text: {
		fontWeight: 'bold',
		fontSize: 16,
		color: '#E9730F',
		marginLeft: 10,
	},

	camera: {
		flex: 5,
		borderRadius: 20,
	},

	topControls: {
		flex: 1,
	},
});