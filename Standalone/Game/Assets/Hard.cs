using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Hard : MonoBehaviour
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
        GlobalControl.difficulty = 3;
        SceneManager.LoadScene((sceneLocate));
    }
}