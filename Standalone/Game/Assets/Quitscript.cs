using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Quitscript : MonoBehaviour
{
    public GameObject button;

    void Start()
    {
    }

    void Update()
    {
    }

    /// <summary>
    /// Quits application when this sprite is clicked. 
    /// </summary> 

    void OnMouseDown()
    {
        Application.Quit();
    }

}