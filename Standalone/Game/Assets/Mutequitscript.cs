using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Collections;
using UnityEngine.SceneManagement;

public class Mutequitscript : MonoBehaviour
{

    // Use this for initialization
    public string sceneLocate;
    AudioSource audioSource;

    void Start()
    {
        audioSource = GetComponent<AudioSource>();
    }

    /// <summary>
    /// Q to quit back to menu mid game. M to mute music.
    /// </summary>

    void Update()
    {
        if (Input.GetKeyDown("m"))
            audioSource.mute = !audioSource.mute;

        if (Input.GetKeyDown("q"))
            SceneManager.LoadScene((sceneLocate));
    }
}
