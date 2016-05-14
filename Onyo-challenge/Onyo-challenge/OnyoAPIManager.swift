//
//  OnyoAPIManager.swift
//  Onyo-challenge
//
//  Created by Matheus Cavalca on 5/13/16.
//  Copyright © 2016 Matheus Cavalca. All rights reserved.
//

import Alamofire
import UIKit

typealias SuccessHandler = (restaurants: [Company]) -> Void
typealias ErrorHandler = (error: NSError!) -> Void

class OnyoAPIManager {
    
    // MARK: -- Singleton
    
    class var sharedInstance: OnyoAPIManager {
        struct Static {
            static var instance: OnyoAPIManager?
            static var token: dispatch_once_t = 0
        }
        
        dispatch_once(&Static.token) {
            Static.instance = OnyoAPIManager()
        }
        
        return Static.instance!
    }
    
    private init() {}
    
    // MARK: - Requisitions
    
    func fetchCompanyList(success: SuccessHandler, failure: ErrorHandler) {
        Alamofire.request(.GET, companyURI(), parameters: nil, encoding:.JSON).responseJSON
            { response in switch response.result {
            case .Success(let response):
                var companiesList = [Company]()
                
                let companiesReturned = response["companies"] as! [[String: AnyObject]]
                for company in companiesReturned {
                    let company = Company(dict: company)
                    companiesList.append(company)
                }
                
                success(restaurants: companiesList)
            case .Failure(let error):
                print("Request failed with error: \(error)")
                failure(error: error)
            }
        }
    }
    
    // MARK: - URL Building
    
    private func companyURI() -> String {
        let path = NSBundle.mainBundle().pathForResource("URIs", ofType: "plist")
        let urls = NSDictionary(contentsOfFile: path!)
        
        let baseURL = urls?.objectForKey("COMPANY_URI") as! String!
        
        return baseURL
    }
}