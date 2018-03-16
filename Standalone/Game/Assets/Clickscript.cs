using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Clickscript : MonoBehaviour
{

    public string sceneLocate;

    void Start()
    {
    }

    void Update()
    {
    }

    /// <summary>
    /// Scene is loaded when sprite is clicked.
    /// </summary>

    void OnMouseDown()
    {
        SceneManager.LoadScene((sceneLocate));
    }

}