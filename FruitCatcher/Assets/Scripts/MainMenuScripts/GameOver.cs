using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using System.IO;
using UnityEngine.SceneManagement;

public class GameOver : MonoBehaviour
{
    [SerializeField] TextMeshProUGUI score_text;
    [SerializeField] TextMeshProUGUI time_text;

    public TMP_InputField Name, id, age, weight, height;
    public TMP_Dropdown gender;

    // Update is called once per frame
    void Start()
    {
        score_text.text = PlayerPrefs.GetInt("Score").ToString();
        time_text.text = PlayerPrefs.GetString("TimeTaken").ToString();
    }

    public void SaveDataInCSV()
    {
        Debug.Log("Saving Data");
        if (Name.text == "" || id.text == "" || age.text == "" || weight.text == "" || height.text == "" || gender.value == 0)
        {
            Debug.Log("Please fill all the fields");
            return;
        }
        string filePath = $"{Application.streamingAssetsPath}/UserData/User.csv";
        Debug.Log(filePath);
        if (!File.Exists(filePath))
        {
            Debug.Log("Does not exist");
            using (StreamWriter sw = File.CreateText(filePath))
            {
                sw.Write("Paitient Name,ID,Gender,Age,Weight,Height,Score,Time Taken,Game Speed");
                string data = $"\n{Name.text},{id.text},{gender.options[gender.value].text},{age.text},{weight.text},{height.text},{PlayerPrefs.GetInt("Score")},{PlayerPrefs.GetString("TimeTaken")},{PlayerPrefs.GetInt("Speed")}";
                sw.Write(data);
                sw.Flush();
                sw.Close();
            }
        }
        else
        {
            Debug.Log("File exists");
            StreamReader sr = new StreamReader(filePath);
            string prevData = sr.ReadToEnd();
            sr.Close();
            string data = prevData + $"\n{Name.text},{id.text},{gender.options[gender.value].text},{age.text},{weight.text},{height.text},{PlayerPrefs.GetInt("Score")},{PlayerPrefs.GetString("TimeTaken")},{PlayerPrefs.GetInt("Speed")}";
            Debug.Log(data);
            Debug.Log($"\n{Name.text},{id.text},{gender.options[gender.value].text},{age.text},{weight.text},{height.text},{PlayerPrefs.GetInt("Score")},{PlayerPrefs.GetString("TimeTaken")},{PlayerPrefs.GetInt("Speed")}");
            using (StreamWriter sw = new StreamWriter(filePath))
            {
                sw.Write(data);
                sw.Flush();
                sw.Close();
            }

        }

    }

}
