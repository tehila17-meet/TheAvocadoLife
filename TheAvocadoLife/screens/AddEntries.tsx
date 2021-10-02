import * as React from 'react';

import { SafeAreaView, StyleSheet, TouchableOpacity, Text, View, TextInput, FlatList } from 'react-native';
import { RootTabScreenProps } from '../types';
import { CollectionItem } from '../components/CollectionItem'
import { ROW, CENTER, TEXT } from '../styles/styles'
import { useState } from 'react';
import { PickCollections } from '../components/pickCollection';
import { DataInputForm } from '../components/InputForm';

export default function AddEntriesScreen({ navigation }: RootTabScreenProps<'AddEntries'>) {

    const [chosenCollection, setChosenCollection] = useState();

    return (
        <View style={styles.container}>
            <View style={styles.header}>
                {
                    !chosenCollection && <Text style={styles.headerText}>What Happened? </Text>
                }
                {
                    chosenCollection && <Text style={styles.headerText}>Enter - {chosenCollection} </Text>
                }
            </View>

            <PickCollections chosenCollection={setChosenCollection} />

            {
                chosenCollection && (<DataInputForm currentCollection={chosenCollection} />)
            }


            <View style={styles.separator} />
        </View>
    );
}


const styles = StyleSheet.create({
    container: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: "#1d2236"

    },

    separator: {
        marginVertical: 30,
        height: 1,
        width: '80%',
    },
    collectionItem: {
        flex: 1,
        flexDirection: "row",
        justifyContent: "space-between",
        marginHorizontal: -10,

    },
    header: {
        ...CENTER,
        height: 70,
        borderBottomWidth: 5,
        borderBottomColor: "#16192e",
        marginBottom: 20
    },
    headerText: {
        ...TEXT,
        fontSize: 24,
        fontWeight: "500",
    },
    content: {
        flex: 1,
        paddingHorizontal: 15,
        paddingVertical: 10,
    },
    chosenCollectionText: {
        ...TEXT
    }
});
