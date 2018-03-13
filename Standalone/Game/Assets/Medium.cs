using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Medium : MonoBehaviour
{
    public string sceneLocate;

    void Start()
    {
    }

    void Update()
    {
    }

    void OnMouseDown()
    {
        GlobalControl.difficulty = 2;
        SceneManager.LoadScene((sceneLocate));
    }
}