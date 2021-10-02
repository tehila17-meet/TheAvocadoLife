
import { SafeAreaView, Button, StyleSheet, TouchableOpacity, TouchableHighlight, Text, View, TextInput, FlatList } from 'react-native';
import * as React from 'react';
import { TEXT } from '../styles/styles';
import { useState, useEffect } from 'react';
import axios from 'axios';

export function DataInputForm({ currentCollection }) {

  //Get Defining Characteristic List
  const [definingtraitOptions, setDefiningCharectaristicOptions] = useState([])
  useEffect(() => {
    axios.get("http://localhost:5000/get_document_names/Defining-Traits")
      .then((response) => setDefiningCharectaristicOptions(response.data.result))
  }, []);

  //Form Data Collection Holders
  const [title, setTitle] = useState()
  const [impactRating, setImpactRating] = useState()
  const [definingtraits, setDefiningCharectaristics] = useState(Array())

  //Form Data Collection Functions
  const handleTitleChange = (e) => {
    setTitle(e.target.value);
  };
  const handleImpactRatingChange = (e) => {
    setImpactRating(e.target.value);
  };
  const handleDefiningCharectaristicAddition = (e) => {
    let definingtraitName = e.target.innerText
    if (!definingtraits.includes(definingtraitName)) {
      definingtraits.push(definingtraitName)
      e.target.style.backgroundColor = '#51caef'
      setDefiningCharectaristics(definingtraits);
    }
    else if (definingtraits.includes(definingtraitName) && definingtraits.length > 0) {
      definingtraits.pop(definingtraitName)
      e.target.style.backgroundColor = 'transparent'
      setDefiningCharectaristics(definingtraits)
    }
  };

  //Form Data Sender
  const sendEntryData = () => {
    axios.post('http://localhost:5000/add_entries', {
      affected_collection: currentCollection,
      title: title,
      impact_rating: impactRating,
      defining_traits: definingtraits
    }).catch(function (error) {
      console.log(error.message);
    });
  };

  return (

    <View style={styles.content}>
      <View style={styles.formInputs}>
        <TextInput
          style={styles.inputFieldText}
          keyboardType="text"
          autoFocus={true}
          placeholder="Title"
          value={title}
          placeholderTextColor="#fff"
          onChange={handleTitleChange} />
        <TextInput
          style={styles.inputFieldNumeric}
          keyboardType="numeric"
          autoFocus={true}
          placeholder="Impact Rating"
          value={impactRating}
          placeholderTextColor="#fff"
          onChange={handleImpactRatingChange}
        />
      </View>
      <View style={styles.definingtraitRow}>
        {definingtraitOptions.map(definingtrait => (
          <View style={styles.definingtraitBox}>
            <TouchableHighlight
              activeOpacity={0.6}>
              <Button title={definingtrait} onPress={handleDefiningCharectaristicAddition} color="transparent" />
            </TouchableHighlight>
          </View>
        ))}
      </View>
      <TouchableOpacity style={styles.buttonSend}>
        <Button title="Add Entry" onPress={sendEntryData} color="transparent" />
      </TouchableOpacity>
    </View>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: "#1d2236"

  },
  formInputs: {
    marginBottom: 30,
    flexDirection: 'row',
    justifyContent: "space-between",

  },
  inputFieldText: {
    height: 30,
    borderRadius: 30,
    paddingHorizontal: 30,
    fontSize: 18,
    color: "#fff",
    backgroundColor: "transparent",
    textAlign: "center",
    textAlignVertical: "center",
    marginRight: 10,
    flex: 1,
    borderColor: "#fff",
    borderWidth: 3
  },
  inputFieldNumeric: {
    height: 30,
    borderRadius: 30,
    paddingHorizontal: 15,
    fontSize: 16,
    color: "#fff",
    backgroundColor: "transparent",
    textAlign: "center",
    textAlignVertical: "center",
    flex: 1,
    borderColor: "#fff",
    borderWidth: 3
  },
  buttonSend: {
    height: 40,
    borderRadius: 25,
    backgroundColor: "#8d015a",
    justifyContent: "center",
    alignItems: "center",
    alignSelf: "center",
    marginTop: 15,
    ...TEXT,
    width: 200
  },
  content: {
    flex: 1,
    paddingHorizontal: 15,
    paddingVertical: 10,
  },
  definingtraitRow: {
    flexDirection: 'row',
    justifyContent: 'space-between'
  },
  definingtraitBox: {
    marginRight: 10,
    marginLeft: 10,
    borderColor: '#51caef',
    borderWidth: 1
  }

});