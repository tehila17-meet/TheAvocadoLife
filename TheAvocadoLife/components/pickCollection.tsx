import * as React from 'react';

import { SafeAreaView, StyleSheet, TouchableOpacity, Text, View, TextInput, FlatList} from 'react-native';
import { RootTabScreenProps } from '../types';
import { CollectionItem } from './CollectionItem'
import { ROW, CENTER, TEXT } from '../styles/styles'
import { useState } from 'react';

export function PickCollections({ chosenCollection }){
  const [collection, setCollection] = useState();
  chosenCollection(collection);

   return ( <View >
     <View style={styles.collectionRow}>
    <CollectionItem
      label="Feelings"
      iconName="heart"
      iconColor="#51caef"
      isActive={collection === "Feelings"}
      setActive={() => setCollection("Feelings")} 
    />
    <CollectionItem
      label="Criticism"
      iconName="frown"
      iconColor="#f15123"
      isActive={collection === "Criticism"}
      setActive={() => setCollection("Criticism")}
    
    />
     <CollectionItem
      label="Compliments"
      iconName="thumbs-up"
      iconColor="#51caef"
      isActive={collection === "Compliments"}
      setActive={() => setCollection("Compliments")}
    
    />
    </View>
    <View style={styles.collectionRow}>

       <CollectionItem
      label="Events"
      iconName="play-circle"
      iconColor="#51caef"
      isActive={collection === "Events"}
      setActive={() => setCollection("Events")}
    
    />
      <CollectionItem
      label="Thought"
      iconName="lightbulb"
      iconColor="#f15123"
      isActive={collection === "Thought"}
      setActive={() => setCollection("Thought")}

    />
      <CollectionItem
      label="Desire"
      iconName="child"
      iconColor="#51caef"
      isActive={collection === "Desire"}
      setActive={() => setCollection("Desire")}
    
    />
    </View>
  </View>)
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: 'center',
      justifyContent: 'center',
      backgroundColor: "#1d2236"
  
    },


    content: {
      flex: 1,
      paddingHorizontal: 15,
      paddingVertical: 10
    },
    collectionRow:{
      flexDirection:'row',
      margin:'10px'
    }
  });