import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, View, SafeAreaView, Image} from 'react-native';
import { useEffect, useRef, useState } from 'react';
import { Camera } from 'expo-camera';
import { shareAsync } from 'expo-sharing';
import * as MediaLibrary from 'expo-media-library';

export default function App() {

	let cameraRef = useRef();
	// setting the camera and media access permissions 
	const [hasCameraPermission, setHasCameraPermission] = useState();
	const [hasMediaPermission, setHasMediaPermission] = useState();
	
	// whether a photo has been clicked or not 
	const [photo, setPhoto] = useState();

	useEffect(() => {
		(async() => {
			const CameraPermission = await Camera.requestCameraPermissionsAsync();
			const MediaLibraryPermission = await MediaLibrary.requestPermissionsAsync();
			setHasCameraPermission(CameraPermission.status === "granted");
			setHasMediaPermission(MediaLibraryPermission.status === "granted");
		})();
	}, []);

	// text to display when camera permission not given 
	if (hasCameraPermission === undefined) {
		return <Text>Requesting permissions... </Text>
	}
	else if (!hasCameraPermission) {
		return <Text>Permission for Camera not granted</Text>
	}

	// taking pictures would be a asynchronous process
	let takePic = async() =>
	{
		let options =
		{
			quality: 1,
			base64: true,
			exif: false
		};

		let newPhoto = await cameraRef.current.takePictureAsync(options);
		setPhoto(newPhoto);
	}

	// if a new photo has been clicked 
	if(photo)
	{
		// share the photo 
		let sharePic = () =>
		{
			shareAsync(photo.uri).then(() => {
				setPhoto(undefined);
			});
		};

		// save a photo to the gallery 
		let savePhoto = () =>
		{
			MediaLibrary.saveToLibraryAsync(photo.uri).then(() => {
				setPhoto(undefined);
			});		
		};

		return
		{
			// so that the screen is well aligned 
			<SafeAreaView style={styles.container}>
				<Image style={styles.preview} source={{ uri: "data:image/jpg;base64" + photo.base64 }}/>
				<Button title='Share' onPress={sharePic}/> 

				{/* can only save a photo if media permission is given */}
				{hasMediaPermission ? <Button title="Save" onPress={savePhoto} />: undefined}
				
				{/* the button to discard the image  */}
				<Button title='Discard' onPress={() => setPhoto(undefined)}/>
			</SafeAreaView>
		};
	}

	return (
		// passing a reference to the camera and taking a pic upon clicking 
		<Camera style={styles.container} ref={cameraRef}>
		<View style={styles.buttonContainer}>
			<Button title='Click Picture' onPress={takePic}/>
		</View>
			<StatusBar style="auto" />
		</Camera>
	);
}

const styles = StyleSheet.create({
	container: {
		flex: 1,
		alignItems: 'center',
		justifyContent: 'center'
	},
	// styling for the camera button 
	buttonContainer:
	{
		backgroundColor: '#fff',
		alignSelf: 'flex-end'
	},
	preview:
	{
		alignSelf: 'stretch',
		flex: 1
	}
});
