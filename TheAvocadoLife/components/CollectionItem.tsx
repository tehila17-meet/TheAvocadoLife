import React from "react";
import { StyleSheet, Text, TouchableOpacity } from "react-native";
import { FontAwesome5 } from "@expo/vector-icons";
import {
    CENTER,
    BOX,
    TEXT_LABEL,
    BG_COLOR,
    HIGHLIGHT_BG_COLOR,
} from "../styles/styles";

export function CollectionItem({ label, iconName, iconColor, isActive, setActive }) {
    return (
        <TouchableOpacity
            style={[
                styles.box,
                {
                    backgroundColor: isActive ? HIGHLIGHT_BG_COLOR : BG_COLOR,
                },
            ]}
            onPress={setActive}
        >
            <FontAwesome5 name={iconName} size={25} color={iconColor} />
            <Text style={styles.label}>{label}</Text>
        </TouchableOpacity>
    );
}

const styles = StyleSheet.create({
    box: {
        ...CENTER,
        ...BOX,
        marginHorizontal: 10,
        width: 80,
        height: 80
    },
    label: {
        ...TEXT_LABEL,
        marginTop: 10,
    },
});