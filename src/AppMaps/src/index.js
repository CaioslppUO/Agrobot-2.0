import React, { Component } from  'react';
import { TouchableOpacity,Text,View } from  'react-native';
import MapView, {Marker} from  'react-native-maps';
import Style from './styles'
import Geolocation from '@react-native-community/geolocation';


export default class Mapa extends Component {
    constructor(props) {
        super(props);
    
        this.state = {
          markers: []
        }
        this.MarkPress = this.MarkPress.bind(this);
        this.ClearPress = this.ClearPress.bind(this);
        this.ShowPress = this.ShowPress.bind(this);
      }

      MarkPress(e) {
        this.setState({
          markers: [
            ...this.state.markers,
            {
              coordinate: e.nativeEvent.coordinate,
            }
          ]
        })
        
      }
      ClearPress(e) {
        this.state.markers.length = 0
        this.setState({
          markers: [
            ...this.state.markers,
          ]
        })
      }

      ShowPress(e) {
        console.log(this.state)
      }
      SetPress(e) {
        // this.state.markers.includes(this.state.region)
      }


    state = {
        region: null,
    }
    async componentDidMount(){
        Geolocation.getCurrentPosition(
            ({ coords: {latitude, longitude}}) => {
                this.setState({
                    region: {
                        latitude, 
                        longitude, 
                        latitudeDelta: 0.009,
                        longitudeDelta: 0.004,
                    }
                })
            },
            () => {},
            {
                timeout: 4000,
                enableHighAccuracy: true,
                maximumAge: 1000
            }
        )
    }
    render() {
        const {region} = this.state
        return(
        <>
            <MapView 
                style = {Style.map}
                initialRegion = {region}
                showsUserLocation
                loadingEnabled
                onPress={this.MarkPress}
            >
                {this.state.markers.map((marker) => {
                    return (<Marker {...marker} />)
                })}

            </MapView>
            <View style = {Style.ContainerButtons}>
                <TouchableOpacity 
                    style={Style.Buttons} 
                    onPress={this.ClearPress}
                >
                    <Text style={Style.TextButton}>Clear</Text>
                </TouchableOpacity>

                <TouchableOpacity 
                    style={Style.Buttons}
                    onPress={this.ShowPress}
                >
                    <Text style={Style.TextButton}>Show</Text>
                </TouchableOpacity>

                <TouchableOpacity 
                    style={Style.Buttons}
                    onPress={this.SetPress}
                >
                    <Text style={Style.TextButton}>Set</Text>
                </TouchableOpacity>

                <TouchableOpacity 
                    style={Style.Buttons}
                    onPress={() => {}}
                >
                    <Text style={Style.TextButton}>Start</Text>
                </TouchableOpacity>

            </View>
        </>
        )
    }
}

